<template>
<div class="modal">
    <div class="content-wrapper">
      <h1>Login</h1>
      <form @submit.prevent="signInAccount">
        <input
          :class="isError ? 'error' : 'success'"
          type="text"
          :value="username"
          placeholder="Enter Username"
          @input="enterUsername"
        />
        <input 
          :class="isError ? 'error' : 'success'"
          type="password"
          key="password" 
          :value="password"
          placeholder="Enter Password"
          @input="enterPassword"
        />

        <button type="submit">
          Login
        </button>
      </form>
      <h4 :class="isError ? 'bold red' : 'bold green'">
        {{ usernameMessage || '' }}
      </h4>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  props: ['username', 'password', 'usernameMessage', 'isError'],
  methods: {
    enterUsername(e) {
      this.$emit('handleUsername', e.target.value)
    },
    enterPassword(e){
      this.$emit('handlePassword', e.target.value)
    },
    signInAccount(){
      this.$emit('signInAccount', this.username, this.password)
    }
    
  }
}
</script>

<style scoped>
.modal {
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.content-wrapper {
  border: 1px solid #757575;
  height: 50%;
  width: 50%;
  border-radius: 6px;
  border: 2px solid;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
  background: linear-gradient(45deg,
        rgb(255, 253, 135),
        rgb(201, 199, 110), 
        rgb(219, 167, 248),
        rgb(197, 90, 255), 
        rgb(166, 0, 255)
  );
}

.content-wrapper,
form {
  display: flex;
  align-items: center;
  justify-content: center;
}

.content-wrapper {
  flex-direction: column;
}

input,
button {
  margin-right: 1em;
  padding: 0.6em 1.2em;
  background-color: white;
  color: rgb(219, 167, 248);
  border: 0;
  border-radius: 6px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}

.error {
  border-color: #e57373;
}

.success {
  border-color: rgb(219, 167, 248);;
}

input {
  border: 2px solid #757575;
  outline: none;
}

button {
  margin-left: 1em;
  cursor: pointer;
}

button:not(:disabled) {
  background-color: white;
}

h4 {
  margin-top: 2em;
}

.bold {
  font-weight: 800;
}

.green {
  color: #a5d6a7;
}
.red {
  color: #e57373;
}
</style>