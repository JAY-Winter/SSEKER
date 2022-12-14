import Router from "next/router";
import styled from "styled-components";

import LargeText from "../../common/LargeText";
import SubtitleText from "../../common/SubtitleText";
import MainButton from "../../common/MainButton";
import Link from 'next/link';
import { useEffect } from 'react';
import { getKeyCookies } from '../../modules/cookie/keyCookies';

const SignupAfterPage = () => {
  const router = Router;

  useEffect(() => {
    if (getKeyCookies("key") === undefined) {
      router.push('/login')
    }
  }, []);

  const moveToTeamList = () => {
    router.push("/team");
  };
  const moveToUserList = () => {
    router.push("/user");
  };

  let vh = 0;
  let vw = 0;
  useEffect(() => {
    vh = window.innerHeight * 0.01;
    vw = window.innerWidth * 0.01;
    document.documentElement.style.setProperty("--vh", `${vh}px`);
    document.documentElement.style.setProperty("--vw", `${vw}px`);
  }, []);

  return (
    <AfterBox>
      <TitleBox>
        <LargeText>준비가 모두 끝났습니다!</LargeText>
      </TitleBox>
      <ButtonBox>
        <SubtitleText>어느 페이지부터 둘러보시겠어요?</SubtitleText>
        <br />
        <SubtitleText>
          아니요! 상세정보를 더 입력하고 싶어요!
        </SubtitleText>
        <SubtitleText>
        <Link href='/usermodify'>정보 수정</Link>
        </SubtitleText>
        <br />
        <MainButton onButtonClick={moveToUserList}>팀원 구하기!</MainButton>
        <MainButton onButtonClick={moveToTeamList}>팀에 들어가기!</MainButton>
      </ButtonBox>
    </AfterBox>
  );
};

export default SignupAfterPage;

const AfterBox = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
  height: calc(var(--vh, 1vh) * 100);
  width: 100vw;
  width: calc(var(--vw, 1vw) * 100);
  color: var(--text-color);
`;

const TitleBox = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: auto;
`;

const ButtonBox = styled.div`
  display: flex;
  flex-direction: column;
  margin: 0px 15px;
  margin-top: auto;
`;
