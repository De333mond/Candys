import {courtEqual} from "@/utils";
import axios from "axios";

export const CourtModule = {
  namespaced: true,

  state() {
    return {
      courtItems: []
    }
  },

  mutations: {
    addItemToState(state, payload) {
      state.courtItems.push(payload)
    },

    setItemsToState(state, payload) {
      state.courtItems = payload;
    },

    setItemByIndex(state, args) {
      state.courtItems[args.index] = args.payload
    },

    setItemQuantity(state, args) {
      console.log(args)
      state.courtItems[args.index].additionalInfo.quantity = args.payload;
    }
  },

  getters: {
    courtLength: state => {
      let len = 0
      state.courtItems.forEach((el) => len += el.additionalInfo.quantity)
      return len
    }
  },

  actions: {
    addItem({state, commit}, payload) {
      let i = state.courtItems.findIndex(el => courtEqual(el, payload))
      if (i !== -1) {
        let el = {...state.courtItems[i]}
        el.additionalInfo.quantity += payload.additionalInfo.quantity;
        commit('setItemByIndex', {index: i, payload: el})
      }
      else
        commit("addItemToState", payload)
    },

    deleteItem({commit, state}, payload) {
      let filtered = state.courtItems.filter((item) => item !== payload)
      commit("setItemsToState", filtered)
    },

    setItemQuantity({commit}, args) {
      console.log({index: args.index, quantity: args.quantity})
      commit('setItemQuantity', {index: args.index, payload: args.quantity})
    },

    makeOrder({commit, state}, {orderId, token}) {
      let requestBody = []
      let products = state.courtItems;

      products.forEach(el => {
        requestBody.push({
          count: el.additionalInfo.quantity,
          title: el.additionalInfo.title ? el.additionalInfo.title : "",
          product: el.item,
          order: orderId,
          filling: el.additionalInfo.fillingId,
        })
      })


      let apiInstance = axios.create({
        headers: {
          "Authorization": "Token " + token,
          "Content-Type": "application/json"
        }
      })



      apiInstance.post("http://localhost:8000/api/orderHasProducts/",
          requestBody
      ).then(res => {
        if (res.status === 201)
          commit('setItemsToState', [])
      }).catch(e => console.log(e))
    }
  }
};