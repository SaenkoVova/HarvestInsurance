export default {
    namespaced: true,
    state: {
        coords: []
    },
    mutations: {
        setCoords(state, payload) {
            state.coords.push(payload)
        },
        unsetCoords(state) {
            state.coords = []
        }
    },
    getters: {
        getCoords: state => state.coords,
        getConvertedCoords: state => state.coords.map(i => [i.lng, i.lat])
    }
}
