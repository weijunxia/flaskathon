<template>
    <div>
        <form>
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
export default {
    name:"FeedForm",
    data: () => ({
        caption:'',
        image:''
    }),
    methods:{
        handleForm(e) {
            // console.log(e.target.value)
            if (e.target.name === "caption"){
                this.caption = e.target.value
            } else {
                this.image = e.target.value
            }
            
        }
    }
}
</script>

<style>

</style>