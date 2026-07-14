class WisprFlowVoiceSummarizerClient:
    def summarize_dictation(self, raw_transcript: str) -> dict:
        clean = raw_transcript.replace("umm", "").replace("err", "").strip()
        return {"structured_summary": f"Cleaned Dictation Summary: {clean}"}