from interactions.models import (
SelfAnswerGroup,
 UserAnswerChoice,
  SelfQuestion
)

def update_dict_with_score(valid_dict: list) -> list:
    
    for dictionary in valid_dict:
	    answer_group = SelfAnswerGroup.objects.get(pk=dictionary['answer_group_pk'])
	
	    answers = [
	        answer.answer_choice for answer in UserAnswerChoice.objects.filter(
	            self_answer_group=answer_group)
	    ]
	
	    question_factors = [
	        answer.question.question_factor for
	        answer in UserAnswerChoice.objects.filter(
	            self_answer_group=answer_group)
	    ]
	
	    final_scores = [answer*question_factor for answer,
	                    question_factor in zip(answers, question_factors)]
	
	    qn_subclasses = [
	        answer.question.ocean_subclass for
	        answer in UserAnswerChoice.objects.filter(
	            self_answer_group=answer_group)
	    ]
	
	    scores = [0, 0, 0, 0, 0]
	    for final_score, question_subclass in zip(final_scores, qn_subclasses):
	        if question_subclass == 'openness':
	            scores[0] = scores[0]+final_score
	        elif question_subclass == 'conscientiousness':
	            scores[1] = scores[1]+final_score
	        elif question_subclass == 'extraversion':
	            scores[2] = scores[2]+final_score
	        elif question_subclass == 'agreeableness':
	            scores[3] = scores[3]+final_score
	        elif question_subclass == 'neuroticism':
	            scores[4] = scores[4]+final_score
	
	    dictionary.update({
	    'score': scores
	    })

    return valid_dict