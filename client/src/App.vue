<template>
  <div id="app">
    <Login 
      v-if="!user"
      @handleUsername="handleUsername"
      @submitUsername="submitUsername"
      :username="username"
      :usernameMessage="usernameMessage"
      :isError="isError"
    />
    <Feed v-else :user="user" @clearUser="clearUser"/>
    <!-- <Messages v-else :user="user" @clearUser="clearUser" /> feed will do here -->
  </div>
</template>

<script>

import Login from './components/Login.vue'
import Feed from './components/Feed.vue'
import {CreateUser, RemoveUser} from './services/users'

export default {
  name: 'App',
  components: {
    Login,
    Feed
  },
  data: () => ({
    username: '', 
    user: JSON.parse(localStorage.getItem('user')) || null,
    usernameMessage: '',
    isError: false
  }),
  methods: {
    handleUsername(value) {
      this.username = value
    },
    async submitUsername() {
      const user = await CreateUser(this.username)
      localStorage.setItem('user', JSON.stringify(user))
      this.user = user
      this.usernameMessage = ''
      this.isError = false
    },
    async clearUser() {
      await RemoveUser(this.user.id)
      localStorage.clear()
      this.user = null
      this.username = ''
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
