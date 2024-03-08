document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('workoutForm').addEventListener('submit', function(e) {
      e.preventDefault();
  
      const goal = document.getElementById('goal').value;
      const level = document.getElementById('level').value;
  
      fetch('/swole', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({goal: goal, level: level}),
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('routine').innerHTML = `<p>${data.routine}</p>`;
      })
      .catch(error => {
        console.error('Error:', error);
      });
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('culinaryQuiz')) {
      const submitBtn = document.getElementById('submitQuiz');
      submitBtn.addEventListener('click', function() {
        let score = 0;
        const totalQuestions = 3;
        const correctAnswers = ['Basil', 'Celery', 'Yeast'];
        const questions = [
          {element: document.querySelector('input[name="question1"]:checked'), correctAnswer: 'Basil'},
          {element: document.querySelector('input[name="question2"]:checked'), correctAnswer: 'Celery'},
          {element: document.querySelector('input[name="question3"]:checked'), correctAnswer: 'Yeast'},
        ];
        
        const resultsContainer = document.getElementById('quizResults');
        resultsContainer.innerHTML = "";
        
        questions.forEach((question, index) => {
          const userAnswer = question.element ? question.element.value : "";
          if (userAnswer === correctAnswers[index]) {
            score++;
            resultsContainer.innerHTML += `<p>Question ${index + 1}: Correct!</p>`;
          } else {
            resultsContainer.innerHTML += `<p>Question ${index + 1}: Incorrect. The correct answer is ${correctAnswers[index]}.</p>`;
          }
        });
        
        resultsContainer.innerHTML += `<p>You scored ${score} out of ${totalQuestions}.</p>`;
      });
    }
  });

