;;------------------------------------------------------------------------------
;; Created: Friday, October 16 2026
;; Author: Kofoed, ESK
;; Description:

(setq x-alt-keysym 'meta)

(setq TERM (getenv "TERM"))
(setq LANG (getenv "LANG"))
(setq LANGUAGE (getenv "LANGUAGE"))
(setq COLORTERM (getenv "COLORTERM"))
(setq GNOME_TERMINAL_SCREEN (getenv "GNOME_TERMINAL_SCREEN"))

(message "Setting up terminal keys")
(bind-key "M-[ B"   'next-line)
(bind-key "M-[ A"   'previous-line)
(bind-key "M-[ C"   'right-char)
(bind-key "M-[ D"   'left-char)

(global-set-key (kbd "[1;5D") #'centaur-tabs-backward)     ; C- <left>
(global-set-key (kbd "[1;5C") #'centaur-tabs-forward)      ; C- <right>

(bind-key "M-[ z"   'backtab)
(bind-key "M-[ z"   'org-shifttab org-mode-map)

;; NOTE Double control keys may not be available (C-c C-,)
(bind-key "C-c ,"   'org-insert-structure-template org-mode-map)
(global-set-key (kbd "M-O Q") #'hydra-shell-stuff/body) ; [f2]

(unless COLORTERM ;; assuming we have an xterm here
  (message "Setting keys and background for xterm")
  (global-set-key (kbd "ø") #'execute-extended-command)   ; M-x
  (global-set-key (kbd "÷") #'kill-ring-save)             ; M-w
  (global-set-key (kbd "ù") #'yank-pop)                   ; M-y
  (global-set-key (kbd "¼") #'beginning-of-buffer)        ; M-<
  (global-set-key (kbd "¾") #'end-of-buffer)              ; M->
  (global-set-key (kbd "ä") #'kill-word)                  ; M-d
  (global-set-key (kbd "í") #'back-to-indentation)        ; M-m
  (global-set-key (kbd "ï") #'ace-window)                 ; M-o
  (global-set-key (kbd "¯") #'dabbrev-expand)             ; M-/
  (global-set-key (kbd "°") #'treemacs)                   ;M-0 (zero)
  (set-face-attribute 'help-key-binding nil :background "#000")
  ;;(set-face-attribute 'help-key-binding nil :background "#000")
  (set-face-attribute 'centaur-tabs-default  nil
                      :foreground "white"
                      :background "black"
                      )
  )

;; End of file
;;----------------------------------------------------------------------------------------------------------------------
;; Local Variables:
;; comment-column: 60
;; End:
;;----------------------------------------------------------------------------------------------------------------------
