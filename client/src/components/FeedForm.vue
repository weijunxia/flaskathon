<template>
    <div>
        <form @submit.prevent="handleSubmit">
            <input 
            name="caption"
            type="text"
            :value="caption"
            placeholder="Enter Caption"
            @input="handleForm"
            />
        <input
            name="image"
            type="text"
            :value="image"
            placeholder="Enter Image"
            @input="handleForm"
            />
            <button type="submit">
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