<template>
  <div class="modal">
    <div class="content-wrapper">
      <form @submit.prevent="submitUsername">
        <input
          :class="isError ? 'error' : 'success'"
          type="text"
          :value="username"
          placeholder="Enter Username"
          @input="enterUsername"
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
  props: {
    username: {
      type: String,
      required: true
    },
    usernameMessage: {
      type: String,
      required: true
    },
    isError: {
      type: Boolean,
      required: true
    }
  },
  methods: {
    enterUsername(e) {
      this.$emit('handleUsername', e.target.value)
    },
    submitUsername() {
      this.$emit('submitUsername')

    },
    logfToFeed() {
      this.$router.push('/feed')
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
