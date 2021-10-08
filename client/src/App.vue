<template>
  <div id="app">
    <div class="nav_bar" v-if="user">
      <Nav :username="user.username" @clearUser="clearUser"/>
    </div>
    <Register 
      v-if="!user"
      @createAccount="createAccount"
      @handleUsername="handleUsername"
      @handlePassword="handlePassword"
      :user='user'
      :username="username"
      :password='password'
      :usernameMessage="usernameMessage"
      :isError="isError"
    />
    <Feed v-else  :user="user" @clearUser="clearUser"/>
    <Login 
      @signInAccount="signInAccount"
      @handleUsername="handleUsername"
      @handlePassword="handlePassword"
      :user='user'
      :username="username"
      :password='password'
      :usernameMessage="usernameMessage"
      :isError="isError"
    />
  </div>
</template>

<script>
import Register from './components/Register.vue'
import Feed from './components/Feed.vue'
import Nav from './components/Nav.vue'
import Login from './components/Login.vue'
import {RegisterUser, LoginUser} from './services/users'

export default {
  name: 'App',
  components: {
    Register,
    Feed,
    Nav,
    Login
  },
  data: () => ({
    username: '', 
    password: '',
    user: JSON.parse(localStorage.getItem('user')) || null,
    usernameMessage: '',
    isError: false
  }),
  methods: {
    handleUsername(value) {
      this.username = value
    },
    handlePassword(value){
      this.password = value
    },
    async createAccount() {
      try {
        const user = await RegisterUser(this.username, this.password)
        localStorage.setItem('user', JSON.stringify(user))
        this.user = user
        this.usernameMessage = ''
        this.isError = false
        
      } catch (error) {
        alert('Error: ', error)
      }
    },
    async signInAccount(){
      try {
        const login = await LoginUser(this.username, this.password)
        console.log(login)
        localStorage.setItem('user', JSON.stringify(login))
        this.user = login
        this.usernameMessage = ''
        this.isError = false
      } catch (error) {
        alert('Error: ', error)
      }
    },
    async clearUser() {
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
