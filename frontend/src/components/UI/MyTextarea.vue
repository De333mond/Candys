<template>
  <div class="ui-textarea-wrapper fl f-col">
    <label class="my-textarea-label" for="my-textarea">{{ label }}</label>
    <textarea
        class="ui-textarea"
        name="my-textarea"
        :value="modelValue"
        :placeholder="placeholder"
        @input="$emit('update:modelValue', $event.target.value)"
    ></textarea>
  </div>
</template>

<script>
export default {
  name: "MyTextarea",
  props: {
    modelValue: {type: String, default: null},
    label: {type: String, default: ""},
    placeholder: {type: String, default: ""},
  }
}
</script>

<style scoped>

  .ui-textarea {
    border: 1px solid #ea746e;
    border-radius: 10px;
    padding: 10px;
    margin-top: 8px;
    height: 150px;
    overflow: hidden;
    transition: .2s ease;
  }

  .ui-textarea:focus {
    box-shadow: 0 0 5px #EB5C54;
    outline: none;
  }

  .my-textarea-label {
    margin: 0;
    font-size: 14px;
    font-family: "Nunito";
  }

  .ui-textarea-wrapper {
    margin: 20px 0;
  }



</style>