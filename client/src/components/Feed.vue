 <template>
  <div class="feed">

      <div>

      <Nav />
      </div>

    <div>
      <FeedForm :user="user"/>
    </div>

    <div class="scroll-feed">
      <FeedCard v-for="post in posts" :key="post.id" :caption="post.caption" :image="post.image" :likes="post.likes" :user_id="post.user_id"/>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import {BASE_URL} from '../globals'
import FeedCard from './FeedCard.vue'
import Nav from '../components/Nav.vue'
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
      const res = await axios.get(`${BASE_URL}/posts`)
      this.posts = (res.data)
      console.log(res.data)
      } catch (error) {
        console.log(error)
        this.error = error
      }
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