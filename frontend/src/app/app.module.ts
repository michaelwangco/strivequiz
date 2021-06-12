import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { TopBarComponent } from './top-bar/top-bar.component';
import { QuestionListComponent } from './question-list/question-list.component';
import { QuizResponseComponent } from './quiz-response/quiz-response.component';
import { QuestionsService } from './questions.service';

@NgModule({
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,
    RouterModule.forRoot([{ path: '', component: QuestionListComponent }])
  ],
  declarations: [
    AppComponent,
    TopBarComponent,
    QuestionListComponent,
    QuizResponseComponent
  ],
  bootstrap: [AppComponent],
  providers: [QuestionsService]
})
export class AppModule {}

/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
