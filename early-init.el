;;; package --- early-init
;;; Commentary:
;; Created: Monday, January 27 2025
;; Author: Erik Kofoed, ESK
;; Description:
;; 

;;; Code:

;; As we use babel to load init-file, org has to be loaded first
;; Disable package.el in favour of straight.el
(setq package-enable-at-startup nil)

;; Get ORG-MODE
(add-to-list 'load-path "~/.emacs.d/lisp") ; NOTE My local lisps

(require 'package)

(when (< emacs-major-version 27)
  (setq gnutls-algorithm-priority "NORMAL:-VERS-TLS1.3")         ; NOTE w/o creates no "gnu", just gnupg
  (require 'gnu-elpa-keyring-update)                             ; NOTE Now accepts gnu archives
)
(add-to-list 'package-archives '("nongnu" . "http://elpa.nongnu.org/nongnu/") t)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(setq package-check-signature nil)

(package-initialize)

(unless package-archive-contents
  (package-refresh-contents))

;; SETUP STRAIGHT

(defvar bootstrap-version)
  (let ((bootstrap-file
         (expand-file-name
          "straight/repos/straight.el/bootstrap.el"
          (or (bound-and-true-p straight-base-dir)
              user-emacs-directory)))
        (bootstrap-version 7))
    (unless (file-exists-p bootstrap-file)
      (with-current-buffer
          (url-retrieve-synchronously
           "https://raw.githubusercontent.com/radian-software/straight.el/develop/install.el"
           'silent 'inhibit-cookies)
        (goto-char (point-max))
        (eval-print-last-sexp)))
    (load bootstrap-file nil 'nomessage))

(straight-use-package 'use-package)
(setq use-package-always-ensure t)
(setq straight-use-package-by-default t)

;; START ORG - correct version
(use-package org) ;; Remainder in main settup.org file

(provide 'early-init)
;;; early-init.el ends here

;; End of file
;;----------------------------------------------------------------------------------------------------------------------
;; Local Variables:
;; comment-column: 60
;; End:
;;----------------------------------------------------------------------------------------------------------------------
