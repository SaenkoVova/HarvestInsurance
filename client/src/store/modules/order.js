export default {
    namespaced: true,
    state: {
        order: null
    },
    mutations: {
        setOrder(state, payload) {
            state.order = payload
        }
    },
    getters: {
        getOrder: state => state.order
    }
}
