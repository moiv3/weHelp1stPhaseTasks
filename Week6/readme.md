# Week 6 Assignment Readme

## This is the Github Repository of Week 6 Assignment.

A simple message board system supporting CRUD. (without the U. Trying to develop that this week!).

Tools used: FastAPI, MySQL

## Features

### 1. User registration

User registers at the Home Page.

### 2. User signin/signout

User signs in from the Home Page.

Upon successful signin, user will be redirected to the Member Page.

User can sign out by clicking the signout link on the member page (or by visiting signout endpoint directly). 

### 3. Message board

User can leave a text message on the Member Page.

The Member Page shows all messages stored in the database from oldest to newest.

By clicking the "Delete" button next to a signed-in user's post, user can delete his/her message.

## Back-end Logic Checks

### 1. Session check

The Member Page endpoint checks for a signin state upon visitng.

If there is no signed-in state, user will be redirected.

### 2. User post check

The delete button only appears for the signed-in user's posts.

