<template>
  <div class="slider-wrapper">
    <div
        class="slider-content"
        :style='{"margin-left": "-" + (currentSlide * 100) + "vw", }'
    >
      <SliderItem
        v-for="item in images"
        :key="item.id"
        :image="item.image"
      />
    </div>
  </div>
</template>

<script>
import SliderItem from "@/components/UI/SliderItem";
import axios from "axios";

export default {
  name: "ImageSlider",
  components: {SliderItem},
  data() {
    return {
      images: [],
      currentSlide: 0,
      fastAnimation: false,
      scrollDown: false,
    }
  },
  mounted() {
    axios.get("http://127.0.0.1:8000/api/carousel/")
        .then(response => {
          this.images = response.data;
        })
        .catch(e => {console.log(e)});

    let cntx = this
    setInterval(() => {
      cntx.increment()
    }, 7000)
  },

  methods: {
    increment() {
      if (this.currentSlide === this.images.length - 1)
        this.scrollDown = true
      if (this.currentSlide === 0 && this.scrollDown)
        this.scrollDown = false

      if (!this.scrollDown)
        this.currentSlide += 1
      else
        this.currentSlide -= 1
    }
  }
}
</script>

<style lang="scss">
  .slider-wrapper {
    overflow: hidden;
    width: 100%;
  }

  .slider-content {
    display: flex;
    transition: all 1.3s ease;
  }



</style>