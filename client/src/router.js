import VueRouter from 'vue-router'
import Login from './components/Login'
import Feed from './components/Feed'


const routes = [
    {path:"/", component:Login, name:'Login'},
    {path:"/feed", component:Feed, name:'Feed'}
]

export default new VueRouter({ 
    routes, 
    mode: 'history'
})