;--------------------------------------------------------------------------------
; Emacs init file
;--------------------------------------------------------------------------------

; Lines below because settings.org contains eval:
(setq custom-file (locate-user-emacs-file "custom-vars.el"))
(load custom-file)
;(add-hook 'kill-emacs-query-functions
;          'custom-prompt-customize-unsaved-options)

(org-babel-load-file "~/.dotfiles/settings.org")

; End of file
;--------------------------------------------------------------------------------
