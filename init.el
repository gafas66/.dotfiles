;--------------------------------------------------------------------------------
; Emacs init file
;--------------------------------------------------------------------------------

; Lines below because settings.org contains eval:
(setq custom-file (locate-user-emacs-file "custom-vars.el"))
(load custom-file)
;(add-hook 'kill-emacs-query-functions
;          'custom-prompt-customize-unsaved-options)

(message "Starting up org-mode init file")
(setq my-org-dir "~/init/org")

(org-babel-load-file "~/.dotfiles/settings.org")

; End of file
;--------------------------------------------------------------------------------
