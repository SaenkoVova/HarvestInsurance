<template>
  <div class="main-banner">
    <div class="container">
      <div class="main-banner__info">
        <div class="main-banner__title">
          <h1>Інновації у сфері страхування відтепер у вашому браузері</h1>
        </div>
        <div class="main-banner__subtitle">
          <p>Бути впевненим у захищеності від втрати врожаю - це право.</p>
        </div>
        <div class="main-banner__btn">
          <router-link :to="'/order'" class="my-btn" style="color: #fff">Оформити поліс</router-link>
        </div>
      </div>
      <div class="main-banner__img">
        <div class="circles">
          <div class="circles__item circles__item--one">
          </div>
          <div class="circles__item circles__item--two">
          </div>
          <div class="circles__item circles__item--three">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

