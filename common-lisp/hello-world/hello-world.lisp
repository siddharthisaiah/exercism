(defpackage #:hello-world
  (:use #:common-lisp)
  (:export #:hello-world)
  (:nicknames #:hw))

(in-package #:hello-world)


(defun (hello-world)
    ;; returns the string "hello world"
    "Hello, World!")
