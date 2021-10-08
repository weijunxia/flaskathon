<template>
  <div class="feed">
    <div class="feed_form">
      <FeedForm :user="user" @getPosts="getPosts"/>
    </div>
    <div class="scroll-feed">
      <FeedCard v-for="post in posts" :key="post.id" :caption="post.caption" :image="post.image" :likes="post.likes" :post_username="post.username" :user="user" :getUserData='getUserData' :post_id="post.id" @getPosts="getPosts"/>
    </div>
  </div>
</template>
<script>

import {GetPosts} from '../services/posts'
import {FindUserById} from '../services/users'
import FeedCard from './FeedCard.vue'
import FeedForm from './FeedForm.vue'


export default {
  name: 'Feed',
  components: {
    FeedCard,
    FeedForm
  },
  props: ['user'],

  data: () => ({
    posts: [],
    error: null
  }),
  mounted: function () {
    this.getPosts()
  },
  methods: {
    async getPosts() {
      try {
        const res = await GetPosts()
        this.posts = (res)
      } catch (error) {
        console.log(error)
        this.error = error
      }
    },
    async getUserData(id) {
      const res = await FindUserById(id)
      console.log('getUserData', res.username)
      return res.username
    }

  }
}
</script>
<style>
.feed {
  display: flex;
  margin-top: 60px;
}
.feed_form {
  display: flex;
  justify-content: center;
  margin-top: 10px;
}
.scroll-feed {
  flex: 1;
  overflow-y: scroll;
  height: 100vh;
}
.item-view {
  padding: 1em;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 1150px;
}
</style>