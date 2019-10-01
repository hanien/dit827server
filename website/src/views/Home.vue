<template>
  <div id="home">
    <header class="nav is-fixed">
      <scrollactive ref="scrollactive" :offset="56" :duration="600">
        <div>
          <b-navbar fixed="top" toggleable="lg" type="dark" class="variant-black">

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
              <b-navbar-nav tabs fill class="navbar-center">

                <b-nav-item><a href="#section-1" class="scrollactive-item">Smart Controls</a></b-nav-item>
                <b-nav-item><a href="#section-2" class="scrollactive-item">Temperature</a></b-nav-item>
                <b-nav-item><a href="#section-3" class="scrollactive-item">Volume</a></b-nav-item>
                <b-nav-item><a href="#section-4" class="scrollactive-item">Light</a></b-nav-item>

              </b-navbar-nav>
            </b-collapse>
          </b-navbar>
        </div>
      </scrollactive>
    </header>

    <main>

      <section id="section-1" class="section">
        <div>
          <b-jumbotron id="jumbo">
            <h4>Smart Controls</h4>
            <br>
            <p>Adjust your car's environment so it's the best for you!</p>
          </b-jumbotron>
        </div>
      </section>

      <section id="section-2" class="section">
        <b-container fluid class="bv-example-row fill">
          <b-row class="fill">
            <b-col id="no1"></b-col>
            <b-col id="no2">
              <p>
                Control the temperature inside your car!
              </p>
            </b-col>
          </b-row>
        </b-container>
      </section>

      <section id="section-3" class="section">
        <b-container fluid class="bv-example-row fill">
          <b-row class="fill">
            <b-col id="no2">
              <p>
                Control the volume inside your car!
              </p>
            </b-col>
            <b-col id="no1"></b-col>
          </b-row>
        </b-container>
      </section>

      <section id="section-4" class="section">
        <b-container fluid class="bv-example-row fill">
          <b-row class="fill">
            <b-col id="no1"></b-col>
            <b-col id="no2">
              <p>
                Control the light inside your car!
              </p>
            </b-col>
          </b-row>
        </b-container>
      </section>
    </main>
  </div>
</template>

<style>
  #home{
    background: black;
  }
  .fill {
    min-height: 100%;
    height: 100%;
  }
  #no1 {
    background-image: url("../assets/temperature.png");
    min-height: 100%;
    height: 100%;
    background-size: cover;
    background-repeat: no-repeat;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  #no2 {
    color: white;
    text-align: center;
    margin: auto;
  }
  .nav.is-fixed {
    position: absolute;
    top: 0;
    left: 0;
  }
  .variant-black{
    background: rgb(0, 0, 0, 0.9);
  }
  .nav.is-fixed .is-active {
    color: rgb(100, 0, 0);
  }
  #jumbo{
   background: rgba(105, 15, 15, 0.062); /* This is for ie8 and below */
   background: rgba(34, 0, 0, 0.7);
   text-align: center;
   margin: auto;
   color: white;
  }
  .navbar-center{
    margin: auto;
  }
  .section {
    height: 500px;
    height: 100vh;
  }
  #section-1{
    background-image: url("https://cdn.motor1.com/images/mgl/Xn2G6/s1/harman-digital-cockpit-ces.jpg");
    background-size: cover;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .fill img {
    flex-shrink: 0;
    min-width: 100%;
    min-height: 100%
}
  .scrollactive-item{
    color:white;
    padding-left: 50px;
    padding-right: 50px;
  }
  .scrollactive-item:hover{
    color:rgb(100, 0, 0);
    text-decoration: none
  }
</style>

<script>
export default {
  name: 'home'
}
</script>
