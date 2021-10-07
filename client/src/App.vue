<template>
  <div id="app">
    <Login 
      :username="username"
      :usernameMessage="usernameMessage"
      :isError="isError"
    />
    <!-- <Messages v-else :user="user" @clearUser="clearUser" /> feed will do here -->
  </div>
</template>

<script>
import Login from './components/Login.vue'

export default {
  name: 'App',
  components: {
    Login,
  },
  data: () => ({
    username: '', 
    // user: JSON.parse(localStorage.getItem('user')) || null,
    usernameMessage: '',
    isError: false
  }),
  methods: {
    async handleUsername(value) {
      this.username = value
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
