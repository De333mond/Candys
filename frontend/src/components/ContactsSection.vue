<template>
  <div class="contacts-container">
    <div class="buttons-container fl">
      <div class="social-button blue">
        <div class="social-button-inner fl">
          <div class="social-button-ico">
            <img src="../assets/images/icons/telegram.png" alt="">
          </div>
          <h2 class="social-button-title">Telegram</h2>
        </div>
      </div>
      <div class="social-button green">
        <div class="social-button-inner fl">
          <div class="social-button-ico">
            <img src="../assets/images/icons/whatsapp.png">
          </div>
          <h2 class="social-button-title">Whatsapp</h2>
        </div>
      </div>
    </div>
    <div class="contacts-text-container">
      <h2>info@candys.com</h2>
      <h2>+7 (912)-345-67-89</h2>
      <h2>Москва, Бережковская наб. 20, стр. 23</h2>
    </div>
  </div>
</template>

<script>
export default {
  name: "ContactsSection"
}
</script>

<style scoped>

  .contacts-container {
    width: 80%;
  }

  .social-button-ico img {
    width: 64px;
  }

  .social-button-inner {
    justify-content: left;
    gap: 60px;
  }

  .social-button {
    width: 400px;
    border-radius: 9px;
    padding: 5px 10px;
  }

  .buttons-container {
    justify-content: space-between;
  }

  .green {
    background-color: #3EC76D;
    transition: all .1s ease;
  }

  .green:hover {
    background-color: #38b461;
  }

  .green:active {
    box-shadow: inset 0px 0px 15px rgba(0, 0, 0, 0.25);
  }

  .blue {
    background: #00A3FF;
  }

  .blue:hover {
    background: #0091e1;
  }

  .blue:active {
    box-shadow: inset 0px 0px 15px rgba(0, 0, 0, 0.25);
  }

  .social-button-inner h2 {
    color: white;
    font-size: 36px;
    margin: .5rem;
    pointer-events: none;
  }



</style>