<template>
  <div class="modal">    
    <div class="content-wrapper">
      <h1>Register</h1>
      <form @submit.prevent="createAccount">
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
          Register
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
  name: 'Register',
  props: ['username', 'password', 'usernameMessage', 'isError'],
  methods: {
    enterUsername(e) {
      this.$emit('handleUsername', e.target.value)
    },
    enterPassword(e){
      this.$emit('handlePassword', e.target.value)
    },
    createAccount(){
      this.$emit('createAccount', this.username, this.password)
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
  background-color: #fafafa;
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
  padding: 0.5em 1.2em;
  border-radius: 6px;
  border: 2px solid transparent;
  transition: all 0.2s ease;
}

.error {
  border-color: #e57373;
}

.success {
  border-color: #a5d6a7;
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
  background-color: #64b5f6;
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
