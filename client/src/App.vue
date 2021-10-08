<template>
  <div id="app">
    <div class="nav_bar" v-if="user">
      <Nav :username="user.username" @clearUser="clearUser"/>
    </div>
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
import Nav from './components/Nav.vue'

import {CreateUser, RemoveUser} from './services/users'

export default {
  name: 'App',
  components: {
    Login,
    Feed,
    Nav
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
body{
  background: rgb(252, 247, 229);
}
.nav_bar{
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;

}
</style>
