<template>
  <div id="app">
    <Login/>
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
    // usernameMessage: '',
    // isError: false
  }),
  methods: {
    // async handleUsername(value, keycode) {
    //   this.username = value
    //   if (keycode === 8) {
    //     this.usernameMessage = ''
    //     this.isError = false
    //   }
    //   if (this.username.length && keycode !== 8) {
    //     try {
    //       const res = FindUsername(this.username)
    //       this.usernameMessage = res.msg
    //       this.isError = false
    //     } catch (error) {
    //       this.usernameMessage = error.response.data.msg
    //       this.isError = true
    //     }
    //   }
    // },
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
