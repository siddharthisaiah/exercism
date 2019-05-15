<?php

class Bob
{
    private $statement;
    
    public function respondTo($statement)
    {
        $this->statement = trim($statement);

        if ($this->isYelledQuestion())
        {
            return "Calm down, I know what I'm doing!";
        }

        if ($this->isQuestion())
        {
            return 'Sure.';
        }

        if ($this->isYelling())
        {
            return "Whoa, chill out!";
        }

        if ($this->isSilence())
        {
            return "Fine. Be that way!";
        }

        return "Whatever.";
    }

    
    private function isQuestion()
    {
        return substr($this->statement, -1) == "?"; // use negative numbers with substr() to begin search from end of string
    }

    
    private function isYelling()
    {
        $statementHasLetters = preg_match("/[a-zA-Z]/", $this->statement); // cannot yell something without letters :)
        $yelling = $this->statement == strtoupper($this->statement);

        return $statementHasLetters && $yelling;
    }

    
    private function isYelledQuestion()
    {
        return $this->isYelling() && $this->isQuestion();
    }

    
    private function isSilence()
    {
        return $this->statement == "";
    }

}
