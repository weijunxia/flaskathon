<template>
    <div>
        <form>
            <input
            :class="isError ? 'error' : 'success'"
            type="text"
            :value="URL"
            placeholder="Enter URL"
            @input="enterUsername"
            />
        <input
            :class="isError ? 'error' : 'success'"
            type="text"
            :value="comment"
            placeholder="Enter Comment"
            @input="enterUsername"
            />
            <button type="submit">
            Blog
            </button>
        </form>
    </div>
</template>

<script>
export default {
    name:"FeedForm"
}
</script>

<style>

</style>