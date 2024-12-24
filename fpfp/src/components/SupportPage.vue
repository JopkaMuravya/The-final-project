<template>
    <div class="main-cont">
        <div class="side-bar">
            <SidebarMenu />
        </div>
        <div class="main-page">
            <main>
                <div class="title">Тех. поддержка</div>
                <div class="title-info">Мы скоро с вами свяжемся!</div>

                <form action="" method="" class="form">
                    <!-- <div class="input-group">
                        <input type="text" name="first_name" id="first-name" placeholder="First name">
                        <label for="first-name">Имя</label>
                    </div>
                    
                    <div class="input-group">
                        <input type="text" name="last_name" id="last-name" placeholder="Last Name">
                        <label for="last-name">Фамилия</label>
                    </div> -->

                    <div class="input-group">
                        <label for="e-mail">e-mail</label>
                        <input type="email" name="e-mail" id="e-mail" placeholder="Е-mail">
                    </div>

                    <div class="textarea-group">
                        <label for="message">Сообщение</label>
                        <textarea name="message" id="message" rows="6" placeholder="Сообщение"></textarea>
                    </div>

                    <div class="button-div">
                        <button type="submit">Отправить</button>
                    </div>
                </form>
            </main>

            <footer>
                <a href="https://github.com/JopkaMuravya/From-people-for-people" target="_blank"><img class="social-media-img" src="../assets/icons/github.svg" alt="GitHub"></a>
            </footer>
        </div>
    </div>

</template>
  
<script>
import axios from 'axios';
import SidebarMenu from './SidebarMenu.vue';
// import { useRouter } from 'vue-router';

// import facebookimg from '../assets/icons/facebook.svg';
// import githubimg from '../assets/icons/github.svg';
// import instagramimg from '../assets/icons/instagram.svg';
// import linkedinimg from '../assets/icons/linkedin.svg';
// import twitterimg from '../assets/icons/twitter.svg';
// import youtubeimg from '../assets/icons/youtube.svg';

export default {
components: {
    SidebarMenu,
},

methods: {
    async login() {
    try {
        const response = await axios.post('http://localhost:8000/api/login/', {
        username: this.username,
        password: this.password,
        });
        const { token } = response.data;
        localStorage.setItem('authToken', token);
        this.errorMessage = '';
        this.router.push('/main');
    } catch (error) {
        this.errorMessage = 'Ошибка входа: Неверный логин или пароль';
        console.error('Ошибка входа:', error.response?.data);
    }
    },
    goToRegister() {
    this.router.push('/'); 
    },
},
};
</script>

<!-- <style scoped>
    .title {
        font-size: 50px;
        font-weight: bold;
        padding: 1.5% 0;
        color: white;
    }

    .title-info {
        padding-bottom: 2%;
        color: white;
    }

    .form {
        display: flex;
        flex-direction: column;
        width: 60%;
        padding: 2%;
    }

    .input-group, .textarea-group {
        padding: 10px;
        font-size: 14px;
        border-radius: 5px;
        border: 1px solid #ccc;

        background-color: white;
    }
</style> -->

<style scoped>
*
{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Arial', sans-serif;
}

.main-cont {
    display: flex;
    flex-direction: row;
}

.main-page {
    flex: 1;
}

main
{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 90%;
    margin: auto;
}

.title
{
    font-size: 50px;
    font-weight: bold;
    padding: 1.5% 0;
    color: white;
}

.title-info
{
	padding-bottom: 2%;
    color: white;
}

.form
{
    display: flex;
    flex-direction: column;
    width: 60%;
    padding: 2%;
}

.input-group, .textarea-group
{
    /* padding: 1% 0;
    color: #d3d3d3; */

    padding: 10px;
    font-size: 14px;
    /* border-radius: 5px;
    border: 1px solid #ccc;
    background-color: white; */
    margin-top: 10px;
}

input, textarea
{
    /* color: inherit;
    width: 100%;
    background-color: transparent;
    border: none;
    border-bottom: 1px solid #757575;
    padding: 1.5%;
    font-size: 20px; */

    color: black;
    width: 100%;
    /* background-color: white; */
    border-radius: 5px;
    border: 1px solid #ccc;
    background-color: white;
    /* border-bottom: 1px solid #757575; */
    padding: 1.5%;
    font-size: 20px;
    margin-top: 10px;
}

/* .textarea-group label
{
    margin-bottom: 50px;
} */

textarea 
{
    resize: none;
    padding-top: 0;
}

/* input:focus, textarea:focus
{
    background-color: transparent;
    outline: transparent;
    border-bottom: 2px solid #69f0ae;
} */

/* input::placeholder, textarea::placeholder
{
    color: transparent;
} */

label
{
    color: white;
    /* position: relative; */
    left: 0.5em;
    /* top: -5\10em; */
	cursor: auto;
    /* transition: 0.3s ease all; */
    font-size: 25px;
    font-weight: 600;
}

/* input:focus ~ label, input:not(:placeholder-shown) ~ label
{
    top: -4em;
    color: #69f0ae;
    font-size: 15px;
} */

/* textarea:focus ~ label, textarea:not(:placeholder-shown) ~ label
{
    top: -10.5em;
    color: #69f0ae;
    font-size: 15px;
} */

.button-div
{
    display: flex;
    justify-content: center;
}

button
{
    margin-top: 10px;
    padding: 2%;
    width: 50%;
    border: 1px solid;
    border-color: #212121;
    border-radius: 5px;
    font-family: inherit;
    font-size: 18px;
    background-color: #0279FE;
    color: white;
    font-weight: 600;
    box-shadow: 0 0 10px #212121;
}

button:hover
{
    background-color: #0050ac;
    /* color: #69f0ae; */
    cursor: pointer;
}


/* Media queries */

@media screen and (max-width: 1200px)
{
    .form
    {
        width: 70%;
    }
}

@media screen and (max-width: 680px)
{
    .form
    {
		width: 90%;
    }
}

@media screen and (max-width: 500px)
{
	.title
	{
		font-size: 40px;
		padding-top: 6%;
	}

	.title-info
	{
		font-size: 13px;
	}
	
	.form
	{
		padding: 6% 4%;
		padding-top: 15%;
	}

	.input-group, .textarea-group
    {
		padding: 3% 0;
	}
	
	input, textarea
	{
		font-size: 15px;
	}

	input:focus ~ label, input:not(:placeholder-shown) ~ label
	{
		top: -3.5em;
		left: 0.1em;
	}
	
	textarea:focus ~ label, textarea:not(:placeholder-shown) ~ label
	{
		top: -8.5em;
		left: 0.2em;
    }
    
    button
    {
        font-size: 15px;
    }
}

footer
{
    display: flex;
    justify-content: space-around;
    align-items: center;
    height: 20vh;
    width: 75%;
    margin: auto;
    opacity: 0.2;
    border-top: 1px solid #212121;
}

footer:hover
{
    animation: fade 0.3s ease;
    opacity: 0.9;
}

.social-media-img
{
    height: 5vh;
}

.codecell-img
{
    height: 10vh;
}

@keyframes fade
{
    0%
    {
        opacity: 0.2;
    }

    100%
    {
        opacity: 0.9;
    }
}

/* Media queries */

@media screen and (max-width: 1295px)
{
    footer
    {
        width: 95%;
    }
}

@media screen and (max-width: 500px)
{
    footer
    {
        opacity: 0.9;
    }
}

body
{
    background-color: #1B263A;
    font-family: 'Overpass Mono', monospace;
    color: #f5f5f5;
}

a
{
    text-decoration: none;
    color: #f5f5f5;
}

a:hover
{
    color: #69f0ae;
}

.hide
{
    display: none;
}

.navbar
{
    height: 10vh;
    display: flex;
    align-items: center;
}

.left-side
{
    display: flex;
    align-items: center;
    flex: 1;
}

.logo
{
    padding: 0 2%;
}

.logo img
{
    height: 7vh;
}

ul
{
    display: flex;
    align-items: center;
    justify-content: space-around;
    width: 50%;
}

li
{
    list-style: none;
}

.left-side li
{
    height: 10vh;
    display: flex;
    align-items: center;
}

.right-side
{
    display: flex;
    justify-content: flex-end;
    align-items: center;
    flex: 0.1;
}

.account
{
    display: flex;
    align-items: center;
    margin-right: 30%;
}

.account:hover
{
    cursor: pointer;
}

.right-side img
{
    height: 5vh;
    border-radius: 50px;
    margin-right: 20%;
}

.dropdown-caret {
    border-top-style: solid;
    border-top-width: 4px;
    border-right: 4px solid transparent;
    border-bottom: 0 solid transparent;
    border-left: 4px solid transparent;
}

.dropdown
{
    position: absolute;
    top: 8vh;
    right: 1vh;
    border: 0.5px solid;
    border-radius: 5px;
    border-color: #212121;
    padding: 0.5%;
    box-shadow: 0 0 10px #212121;
    background-color: black;
    z-index: 2;
}

.user-name
{
    margin-bottom: 5%;
    padding: 2%;
    width: 180px;
    border-bottom: 1px solid #212121;
    color: #757575;
}

.user-name:hover
{
    cursor: default;
}

.dropdown ul
{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    width: 180px;
}

.dropdown li
{
    padding: 2%;
    width: 180px;
}

.dropdown li:hover
{
    background-color: #424242;
    border-radius: 3px;
}


/* Media query */

@media screen and (max-width: 1200px)
{
    .logo
    {
        flex: 1;
        display: flex;
        justify-content: center;
    }

    .burger-menu
    {
        flex: 0.1;
        padding-left: 2%;
    }

    .burger-menu:hover
    {
        cursor: pointer;
    }
    
    .line-1, .line-2, .line-3
    {
        width: 25px;
        height: 3px;
        background-color: #f5f5f5;
        margin: 5px;
    }

    .burger-menu-dropdown
	{
		display: flex;
		flex-direction: column;
		position: absolute;
		top: 10vh;
		left: 0;
		width: 100%;
		margin: auto;
		z-index: 1;
		background-color: rgba(0, 0, 0, 0.9); /* RGB of black */
	}

	.burger-menu-dropdown li
	{
		width: 90vw;
		display: flex;
		justify-content: center;
	}

	.burger-menu-dropdown li:hover
	{
		color: #69f0ae;
		background-color: rgba(66, 66, 66, 0.3);
		border-radius: 8px;
	}

	.hide-burger-menu
	{
		display: none;
	}
}
</style>  