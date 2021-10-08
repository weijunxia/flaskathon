<template>
  <div class="feed_card">
    <div class="card_image">
      <img :src="image"/>
      <button @click="deletePost(post_id)">X</button>
    </div>
    <div class="card_likes">
      <p>❤️ {{likes}} likes</p>
    </div>
    <div class="card_caption">
      <p class="user_name">{{post_username}}</p>
      <p>{{caption}}</p>
    </div>
  </div>

</template>

<script>
import {FindUserById} from '../services/users'
import {DeletePost} from '../services/posts'

export default {
  name: 'FeedCard',
  props: ['caption', 'image', 'likes', 'post_username', 'user', 'post_id', 'getPosts'],
  data: ()=>({
    users_post_id: []
  }),
  methods: {
    async userIdToUserName(id){
      const res =  await FindUserById(id)
      // this.users_post_id = res.username
      console.log(res)
      return res.username
    },
    async deletePost(post_id){
      if (this.user.username === this.post_username) {
        const res = await DeletePost(post_id)
        this.$emit('getPosts')
        return res
      }
    }
  }
}
</script>

<style>


.feed_card {
  border: 1px solid;
  border-radius: 8px;
  max-width: 50vw;
  margin: 1em auto;
  cursor: pointer;
  transition: all .2s ease;
}

.feed_card:hover{
  opacity: .8;
}

.card_image img{
  width:  100%;
  height: 35em;
  object-fit: cover;
  border-radius: 4px 4px 0 0;
  /* border-radius: 50%; */
}


</style>