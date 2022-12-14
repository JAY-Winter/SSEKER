import React from "react";
import styled from "styled-components";

import NanumSquareBold from "../modules/fonts/NanumSquareNeoBold";

const ModifyHeader = ({
  name,
  nameHandler,
  sendData,
}: {
  name: string;
  nameHandler: Function;
  sendData: Function;
}) => {
  return (
    <TitleBox>
      <NanumSquareBold />
      <ContentBox>
        <InputBox
          placeholder={name ? name : `이름을 입력하세요`}
          onChange={(e) => nameHandler(e, 0)}
        />

          <Edit className="bx bx-check" onClick={()=>{sendData()}} />
      </ContentBox>
    </TitleBox>
  );
};

export default ModifyHeader;

const Edit = styled.i`
  font-size: 35px;

  &:hover {
    color: var(--primary-color-light);
    cursor: pointer;
  }
`;

const InputBox = styled.input`
  border: solid 2px var(--primary-color);
  width: 90%;
  padding: 1em;
  margin-right: 1em;
  border-radius: 20px;
`;

const ContentBox = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;

  & a {
    text-decoration: none;
    color: black;
  }
`;

const TitleBox = styled.div`
  margin: 5em 0 2.5em 0;
  width: 100%;
  padding: 1em 2em;
  position: relative;
  overflow: hidden;
  transform: translate3d(0, 0, 0);
`;
