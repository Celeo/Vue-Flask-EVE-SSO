<template>
<div id="app">
  <div id="start" v-if="!back">
    <h2>Click <a :href="url">here</a> to log into EVE using the SSO</h2>
  </div>
  <div id="back" v-cloak v-if="back">
    <h2 v-if="!error && !valid">Completing your login, please wait ...</h2>
    <h2 style="color: red" v-cloak v-if="error">
      An error occurred with your login!<br>
      Want to <a v-link="{name: 'login'}">try again</a>?
    </h2>
    <h2 v-cloak v-if="valid && !error">Login successful <strong>{{ character_name }}</strong>, redirecting you ...</h2>
  </div>
</div>
</template>

<script>
import rs from 'jsrsasign'
import config from './config.js'
import URI from 'urijs'


export default {
  data() {
    return {
      back: false,
      url: '',
      error: false,
      valid: false
    }
  },
  route: {
    canReuse: false
  },
  created() {
    let code = new URI(window.location.href).search(true)['code']
    if (code) {
      this.back = true
      try {
        let token = ''
        this.$http.post('http://localhost:5000/', {'code': code}).then((response) => {
          token = response.data
          try {
            let isValid = rs.jws.JWS.verifyJWT(token, config['secret_key'], {alg: ['HS256']})
            if (isValid) {
              let payloadObj = rs.jws.JWS.readSafeJSONString(rs.b64utoutf8(token.split(".")[1]))
              this.character_name = payloadObj['character_name']
              localStorage.setItem('character_name', this.character_name)
              this.valid = true
              this.error = false
              let router = this.$router
              setTimeout(function() {
                router.go({name: 'app'})
              }, 3000)
            } else {
              this.error = true
            }
          }
          catch (err) {
            console.error('Exception thrown in JWT processing: ' + err)
            this.error = true
          }
        }, (response) => {
          this.error = true
          console.error('The backend returned an error: ' + response.data['message'])
        })
      } catch (err) {
        console.error('Misc exception thrown: ' + err)
        this.error = true
      }
    } else {
      this.$http.get('http://localhost:5000/').then((response) => {
        this.url = response.data.url
      })
    }
  }
}
</script>

<style scoped>
#app {
  text-align: center;
}
</style>
