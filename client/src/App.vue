<template>
  <div id="app">
    <Login 
      @handleUsername="handleUsername"
      :username="username"
      :usernameMessage="usernameMessage"
      :isError="isError"
    />
    <Feed />
    <!-- <Messages v-else :user="user" @clearUser="clearUser" /> feed will do here -->
  </div>
</template>

<script>
import Login from './components/Login.vue'
import Feed from './components/Feed.vue'

export default {
  name: 'App',
  components: {
    Login,
    Feed
  },
  data: () => ({
    username: '', 
    usernameMessage: '',
    isError: false
  }),
  methods: {
    handleUsername(value) {
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
