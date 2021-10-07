 <template>
  <div class="feed">
    <div class="scroll-feed">
      <FeedCard v-for="image in stockImages" :key="image.id" :photo="image" />
    </div>
    <div class="item-view" v-if="selectedImage">
      <DetailView :photo="selectedImage"/>
    </div>
    <div class="item-view" v-else>
      <div>
        <img src="../assets/logo.png" />
      </div>
      <h3>No Photo Selected</h3>
    </div>
  </div>
</template>
<script>
import FeedCard from './FeedCard.vue'

export default {
  name: 'Feed',
  components: {FeedCard},
  data: () => ({
    images: [],
    selectedImage: null,
  }),
  mounted: function () {
    this.getImages()
  },
  methods: {
    async getImages() {
      this.images = (res.data)
      console.log(res.data[0].user.username)
    },
    async selectPhoto(photoId) {    
    }
  }
}
</script>
<style>
.feed {
  display: flex;
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