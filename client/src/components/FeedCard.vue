<template>
  <div class="feed_card">
    <div class="card_image">

    </div>
    <div class="card_likes">
    </div>
    <div class="card_caption">

    </div>
  </div>

</template>

<script>
export default {
  name: 'FeedCard',
  props: {},
  methods: {
    
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

.card_image {
  border-radius: 50%;
}


</style>