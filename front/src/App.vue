<template>
<div id="app">
  <h3>Welcome to the site, <strong>{{ name }}</strong></h3>
  <h4>Click <a @click="logout">here</a> to log out</h4>
</div>
</template>

<script>
export default {
  data() {
    return {
      name: ''
    }
  },
  created() {
    this.name = localStorage.getItem('character_name')
  },
  methods: {
    logout: function() {
      localStorage.removeItem('character_name')
      this.$router.go({name: 'login'})
    }
  }
}
</script>

<style>
[v-cloak] {
  display: none;
}
.fade-transition {
  transition: opacity .5s ease;
}
.fade-enter, .fade-leave {
    opacity: 0;
}
a {
  cursor: pointer;
}
</style>
