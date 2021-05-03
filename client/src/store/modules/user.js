import http from "@/util/http";

const userEndpoints = {
    REGISTER: `register/`,
    LOGIN: 'login/',
    GET_USER_INFO: 'user'
}

export default {
    namespaced: true,
    state: {
        isAuthorized: !!localStorage.getItem('token'),
        user: {}
    },
    mutations: {
        setUser(state, payload) {
            state.user = payload;
            state.isAuthorized = true;
            localStorage.setItem('token', payload.token);
        },
        unsetUser(state) {
            state.user = null;
            state.isAuthorized = false;
            localStorage.removeItem('token');
        }
    },
    actions: {
        signUp({commit}, payload) {
            return new Promise(resolve => {
                http.post(userEndpoints.REGISTER, payload)
                    .then(res => {
                        const user = {
                            birthDate: res.data.birth_date,
                            docs: res.data.docs,
                            email: res.data.email,
                            firstName: res.data.first_name,
                            secondName: res.data.second_name,
                            thirdName: res.data.third_name,
                            phone: res.data.phone,
                            token: res.data.token
                        }
                        commit('setUser', user);
                        resolve()
                    })
                    .catch(err => {
                        console.log(err.response.data)
                    })
            })
        },
        logIn({commit}, payload) {
            return new Promise(resolve => {
                http.post(userEndpoints.LOGIN, payload)
                    .then(res => {
                        const user = {
                            email: res.data.email,
                            token: res.data.token
                        }
                        commit('setUser', user)
                        resolve()
                    })
            })
        },
        loadUserInfo({commit}) {
            return new Promise(resolve => {
                http.get(userEndpoints.GET_USER_INFO, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`
                    }
                })
                    .then(res => {
                        const user = {
                            birthDate: res.data.birth_date,
                            docs: res.data.docs,
                            email: res.data.email,
                            firstName: res.data.first_name,
                            secondName: res.data.second_name,
                            thirdName: res.data.third_name,
                            phone: res.data.phone,
                            token: res.data.token
                        }
                        commit('setUser', user)
                        resolve()
                    })
            })
        }
    },
    getters: {
        getAuthState: state => state.isAuthorized,
        getName: state => state.user.firstName,
        getUser: state => state.user
    }
}
