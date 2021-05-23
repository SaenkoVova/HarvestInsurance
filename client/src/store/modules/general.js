export default {
    namespaced: true,
    state: {
        drawerMiniVariant: !!localStorage.getItem('drawerMiniVariant'),
        authPopupActive: false,
        notRegisteredUser: false
    },
    mutations: {
        setDrawerVariant(state, payload) {
            state.drawerMiniVariant = payload;
            payload === true ? localStorage.setItem('drawerMiniVariant', true.toString()) : localStorage.removeItem('drawerMiniVariant')
        },
        setNotRegisteredUser(state, payload) {
          state.notRegisteredUser = payload;
        },
        togglePopup(state) {
            state.authPopupActive = !state.authPopupActive
        }
    },
    getters: {
        getDrawerMiniVariant: state => state.drawerMiniVariant,
        getAuthPopupActive: state => state.authPopupActive,
        getNotRegisteredUser: state => state.notRegisteredUser
    }
}
