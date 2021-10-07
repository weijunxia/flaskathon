 <template>
  <div class="feed">
    <div class="scroll-feed">
      <FeedCard v-for="post in posts" :key="post.id" :photo="post" />
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import {BASE_URL} from '../globals'
import FeedCard from './FeedCard.vue'

export default {
  name: 'Feed',
  components: {FeedCard},
  data: () => ({
    posts: [],
  }),
  mounted: function () {
    this.getPosts()
  },
  methods: {
    async getPosts() {
      const res = await axios.get(`${BASE_URL}/posts`)
      this.posts = (res.data)
      console.log(res.data)
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