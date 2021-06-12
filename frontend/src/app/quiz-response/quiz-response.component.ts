import { Component, OnInit } from '@angular/core';
import { Input } from '@angular/core';
import { Question } from '../questions';

@Component({
  selector: 'app-quiz-response',
  templateUrl: './quiz-response.component.html',
  styleUrls: ['./quiz-response.component.css']
})
export class QuizResponseComponent implements OnInit {
  @Input() question!: Question;
  constructor() {}

  ngOnInit() {}
}
