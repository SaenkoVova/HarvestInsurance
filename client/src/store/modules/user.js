import http from "@/util/http";

const userEndpoints = {
    REGISTER: `register/`
}

export default {
    namespaced: true,
    state: {
        isAuthorized: false,
        user: null
    },
    mutations: {
        setUser(state, payload) {
            state.user = payload;
            state.isAuthorized = true;
        }
    },
    actions: {
        signUp({commit}, payload) {
            return new Promise((resolve) => {
                http.post(userEndpoints.REGISTER, payload)
                    .then(res => {
                        commit('setUser');
                        resolve(res)
                    })
            })
        }
    },
    getters: {
        getAuthState: state => state.isAuthorized
    }
}
