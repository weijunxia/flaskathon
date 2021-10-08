<template>
    <div class='feed_form'>
        <form @submit.prevent="handleSubmit" class="feed_form_form">
            <input 
            name="caption"
            type="text"
            :value="caption"
            placeholder="Enter Caption"
            @input="handleForm"
            class="feed_form_input"
            />
        <input
            name="image"
            type="text"
            :value="image"
            placeholder="Enter Image"
            @input="handleForm"
            class="feed_form_input"
            />
            <button type="submit" class="feed_form_button">
            Blog
            </button>
        </form>
    </div>
</template>

<script>
import {CreatePost} from '../services/posts'

export default {
    name:"FeedForm",
    data: () => ({
        caption:'',
        image:'',
        likes: 2
    }),
    props:['user'],
    methods:{
        handleForm(e) {
            // console.log(e.target.value)
            if (e.target.name === "caption"){
                this.caption = e.target.value
            } else {
                this.image = e.target.value
            }
            
        },
        async handleSubmit() {
            const feedData = await CreatePost({'user_id':this.user.id, 'caption':this.caption, 'image':this.image, 'likes':this.likes})
            this.$forceUpdate()
            return feedData
            
        }
    }
}
</script>

<style>

</style>