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
(bind-key "M-[ z"   'backtab)

;; End of file
;;----------------------------------------------------------------------------------------------------------------------
;; Local Variables:
;; comment-column: 60
;; End:
;;----------------------------------------------------------------------------------------------------------------------
