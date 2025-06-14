from enum import Enum


class ProgramRuleActionProgramRuleActionType(str, Enum):
    ASSIGN = "ASSIGN"
    CREATEEVENT = "CREATEEVENT"
    DISPLAYKEYVALUEPAIR = "DISPLAYKEYVALUEPAIR"
    DISPLAYTEXT = "DISPLAYTEXT"
    ERRORONCOMPLETE = "ERRORONCOMPLETE"
    HIDEFIELD = "HIDEFIELD"
    HIDEOPTION = "HIDEOPTION"
    HIDEOPTIONGROUP = "HIDEOPTIONGROUP"
    HIDEPROGRAMSTAGE = "HIDEPROGRAMSTAGE"
    HIDESECTION = "HIDESECTION"
    SCHEDULEMESSAGE = "SCHEDULEMESSAGE"
    SENDMESSAGE = "SENDMESSAGE"
    SETMANDATORYFIELD = "SETMANDATORYFIELD"
    SHOWERROR = "SHOWERROR"
    SHOWOPTIONGROUP = "SHOWOPTIONGROUP"
    SHOWWARNING = "SHOWWARNING"
    WARNINGONCOMPLETE = "WARNINGONCOMPLETE"

    def __str__(self) -> str:
        return str(self.value)
