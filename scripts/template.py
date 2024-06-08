html = """
<style>
  .w-full.h-full.min-h-screen.relative div.py-4.px-4.lg\:px-6 {
    padding: 0 !important;
  }

  .sm\:hidden .mt-8.mb-8.px-8 {
    padding: 0 !important;
    margin-top: 0 !important;
  }

  .btn-recomecar {
    background-color: #41ff80 !important;
  }

  .quiz-container {
    background-color: #3a3f4b;
    padding: 30px;
    border-radius: 0;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    width: 100%;
    max-width: 100%;
    margin: 0 auto;
    color: #ffff;
    font-family: "Arial", sans-serif;
  }

  .quiz-container .question-info {
    font-size: 20px;
    margin-bottom: 20px;
    text-align: center;
    background-color: #61dafb;
    color: #282c34;
    padding: 10px;
    border-radius: 12px;
    font-weight: bold;
  }

  .quiz-container .question {
    font-size: 22px;
    margin-bottom: 20px;
  }

  .quiz-container .answers label {
    display: block;
    margin: 8px 0;
    background: #20232a;
    padding: 10px;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s;
  }

  .quiz-container input[type="radio"] {
    margin-right: 10px;
    cursor: pointer;
    -webkit-appearance: none;
    -moz-appearance: none;
    width: 14px;
    height: 14px;
    vertical-align: middle;
    margin: 0 10px;
    border-radius: 50%;
    background-clip: content-box;
    background-color: rgba(255, 252, 229, 1);
  }

  .quiz-container input[type="radio"]:checked {
    background-color: #47b0ee;
    padding: 3px;
    width: 14px;
    height: 14px;
    border: 2px solid #47b0ee;
  }

  .quiz-container .answers label:hover {
    background-color: #282c34;
  }

  .quiz-container .nav-buttons {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    margin-top: 30px;
  }

  .quiz-container button {
    padding: 12px 24px;
    border: none;
    background-color: #61dafb;
    color: #282c34;
    border-radius: 8px;
    cursor: pointer;
    flex-grow: 1;
    font-size: 16px;
    font-weight: bold;
    transition: background-color 0.3s, transform 0.2s;
  }

  .quiz-container button:hover {
    background-color: #4fa1f3;
    transform: translateY(-2px);
  }

  .quiz-container button:disabled {
    background-color: #555;
    cursor: not-allowed;
    transform: none;
  }

  .quiz-container .correct {
    color: #98c379;
  }

  .quiz-container .incorrect {
    color: #e06c75 !important;
  }

  .quiz-container .feedback {
    display: none;
    margin: 0px 1rem;
    margin-top: 0px;
    margin-top: 0.5rem;
    color: #56b6c2;
    padding: 10px 6px 6px 12px;
    border-top: 1px solid #817878;
  }

  .quiz-container .feedback::before {
    content: "* ";
  }

  .quiz-container .hidden {
    display: none;
  }
</style>

<audio
  src="not_found.mp3"
  type="audio/mp3"
  onerror="window.checkAnswer=function(e,t,c){let i;document.querySelectorAll('.quiz-container').forEach((e=>{e.checkVisibility()&&(i=e)}));i.querySelectorAll('#question'+e+' .answers input').forEach((function(e,i){e.disabled=!0,i===t-1?e.parentElement.classList.add('correct'):e.parentElement.classList.remove('correct','incorrect'),e===c&&i!==t-1&&e.parentElement.classList.add('incorrect')}));i.querySelectorAll('#question'+e+' .feedback').forEach((function(e,c){c!==t-1&&e.classList.add('incorrect'),e.style.display='block'}))},window.nextQuestion=function(e,t){let c;document.querySelectorAll('.quiz-container').forEach((e=>{e.checkVisibility()&&(c=e)})),c.querySelector('#question'+e).classList.add('hidden'),c.querySelector('#question'+t).classList.remove('hidden')},window.previousQuestion=function(e,t){let c;document.querySelectorAll('.quiz-container').forEach((e=>{e.checkVisibility()&&(c=e)})),c.querySelector('#question'+e).classList.add('hidden'),c.querySelector('#question'+t).classList.remove('hidden')},window.restartQuiz=function(){let e;document.querySelectorAll('.quiz-container').forEach((t=>{t.checkVisibility()&&(e=t)}));e.querySelectorAll('input[type=\'radio\']').forEach((function(e){e.checked=!1,e.disabled=!1,e.parentElement.classList.remove('correct','incorrect')}));e.querySelectorAll('.feedback').forEach((function(e){e.style.display='none'})),e.querySelector('#question1').classList.remove('hidden');const t=e.querySelectorAll('.question-container:not(#question1)');for(const e of t)e.classList.add('hidden')};"
></audio>

<div class="quiz-container">

</div>
"""
