<template>
  <div class="ui-input-wrapper fl f-col">
    <label class="my-input-label" for="my-input">{{ label }}</label>
    <input
        class="ui-input"
        name="my-input"
        :type="type"
        :value="modelValue"
        :placeholder="placeholder"
        @input="$emit('update:modelValue', $event.target.value)"
        :class="{'invalid': error}"
    >
    <small class="error-message" v-if="error">{{ errorMessage }}</small>
  </div>
</template>

<script>
export default {
  name: "MyInput",
  props: {
    modelValue: {type: String, default: null},
    label: {type: String, default: ""},
    placeholder: {type: String, default: ""},
    type: {type: String, default: "text"},
    error: {type: Boolean, default: false},
    errorMessage: {type: String, default: "input error!"}
  }
}
</script>

<style scoped>

  .ui-input {
    border: 1px solid #ea746e;
    border-radius: 10px;
    padding: 10px;
    margin-top: 8px;
    transition: .2s ease;
  }

  .ui-input:focus {
    box-shadow: 0 0 5px #EB5C54;
    outline: none;
  }

  .my-input-label {
    margin: 0;
    font-size: 14px;
    font-family: Nunito;
  }

  .ui-input-wrapper {
    width: 100%;
    margin-top: 20px;
  }

  .error-message {
    font-family: Nunito;
    color: red;
    margin-top: 5px;
  }


</style>