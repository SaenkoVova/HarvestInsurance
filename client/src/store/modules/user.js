import http from "@/util/http";

const userEndpoints = {
    REGISTER: `register/`,
    LOGIN: 'login/',
    GET_USER_INFO: 'user',
    GET_USER_DOCS: 'loadUserDocuments/',
    GET_NOTIFICATIONS: 'loadNotifications/',
    READ_NOTIFICATIONS: 'readNotifications/',
    DELETE_NOTIFICATION: 'deleteNotification/'
}

export default {
    namespaced: true,
    state: {
        isAuthorized: !!localStorage.getItem('token'),
        user: {},
        docs: [],
        notifications: []
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
        },
        setDocuments(state, payload) {
            state.docs = payload
        },
        setNotifications(state, payload) {
            state.notifications = payload;
        }
    },
    actions: {
        readNotifications({dispatch}) {
            return new Promise(resolve => {
                http.get(userEndpoints.READ_NOTIFICATIONS, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`
                    }
                })
                    .then(res => {
                        dispatch('loadNotifications')
                        console.log(res)
                        resolve(res.data)
                    })
            })
        },
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
                http.get(userEndpoints.GET_USER_INFO)
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
        },
        loadNotifications ({commit}) {
          return new Promise(resolve => {
              http.get(userEndpoints.GET_NOTIFICATIONS, {
                  headers: {
                      Authorization: `Bearer ${localStorage.getItem('token')}`
                  }
              })
                  .then(res => {
                      commit('setNotifications', res.data);
                      resolve()
                  })
          })
        },
        loadUserDocs({commit}) {
            return new Promise(resolve => {
                http.get(userEndpoints.GET_USER_DOCS, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`
                    }
                })
                    .then(res => {
                        commit('setDocuments', res.data)
                        resolve()
                    })
            })
        },
        deleteNotification({dispatch}, payload) {
            return new Promise(resolve =>  {
                http.get(userEndpoints.DELETE_NOTIFICATION, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('token')}`,
                    },
                    params: {
                        notificationId: payload
                    }
                })
                    .then(() => {
                        dispatch('loadNotifications')
                        resolve()
                    })
            })
        }
    },
    getters: {
        getAuthState: state => state.isAuthorized,
        getName: state => state.user.firstName,
        getUser: state => state.user,
        getDocs: state => state.docs,
        getNotifications: state => state.notifications
    }
}
