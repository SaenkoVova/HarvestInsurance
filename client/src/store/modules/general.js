export default {
    namespaced: true,
    state: {
        drawerMiniVariant: !!localStorage.getItem('drawerMiniVariant'),
    },
    mutations: {
        setDrawerVariant(state, payload) {
            state.drawerMiniVariant = payload;
            payload === true ? localStorage.setItem('drawerMiniVariant', true.toString()) : localStorage.removeItem('drawerMiniVariant')
        }
    },
    getters: {
        getDrawerMiniVariant: state => state.drawerMiniVariant
    }
}
